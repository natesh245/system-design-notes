/**
 * Lab 4: Native HTTP Server
 * 
 * Demonstrates a native HTTP server in Node.js handling raw request-response states,
 * header parsing, routing, and returning standard status codes.
 * Includes an interactive demonstration of the Idempotency Key Pattern.
 * 
 * Run: node 04-http-server/server.js
 * Open: http://localhost:3000
 */

const http = require('http');
const url = require('url');

const PORT = 3000;

// Simple in-memory storage for idempotency keys to simulate Redis
const processedRequests = new Map(); 

const server = http.createServer((req, res) => {
    const parsedUrl = url.parse(req.url, true);
    const pathname = parsedUrl.pathname;
    
    // Set default headers (JSON, CORS)
    res.setHeader('Content-Type', 'application/json');
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('X-Powered-By', 'NodeJS-Networking-Lab');

    console.log(`💻 [${new Date().toISOString()}] ${req.method} ${pathname}`);

    // Route 1: Home/Welcome
    if (pathname === '/' && req.method === 'GET') {
        res.writeHead(200);
        res.end(JSON.stringify({
            message: "Welcome to the Native HTTP Server Lab!",
            endpoints: {
                home: "GET /",
                inspect_headers: "GET /headers",
                custom_status: "GET /status?code=429",
                idempotent_post: "POST /payment (Requires 'idempotency-key' header)"
            }
        }));
    }
    
    // Route 2: Inspect Headers
    else if (pathname === '/headers' && req.method === 'GET') {
        res.writeHead(200);
        res.end(JSON.stringify({
            message: "Incoming Request Headers captured by server:",
            headers: req.headers
        }));
    }
    
    // Route 3: Status Code Simulation
    else if (pathname === '/status' && req.method === 'GET') {
        const codeQuery = parseInt(parsedUrl.query.code) || 200;
        
        // Validate if standard status code
        if (http.STATUS_CODES[codeQuery]) {
            res.writeHead(codeQuery);
            res.end(JSON.stringify({
                statusCode: codeQuery,
                statusMessage: http.STATUS_CODES[codeQuery]
            }));
        } else {
            res.writeHead(400);
            res.end(JSON.stringify({
                error: "Invalid status code requested."
            }));
        }
    }

    // Route 4: Idempotent POST Payment simulation
    else if (pathname === '/payment' && req.method === 'POST') {
        const idempotencyKey = req.headers['idempotency-key'];

        if (!idempotencyKey) {
            res.writeHead(400);
            res.end(JSON.stringify({
                error: "Bad Request: Missing 'idempotency-key' header. Non-idempotent retries are forbidden."
            }));
            return;
        }

        // Check if idempotency key has been used before (SETNX logic)
        if (processedRequests.has(idempotencyKey)) {
            const cachedResponse = processedRequests.get(idempotencyKey);
            
            res.writeHead(200);
            res.end(JSON.stringify({
                message: "Duplicate request detected! Returning cached response to prevent duplicate charge.",
                idempotentKey: idempotencyKey,
                originalResponse: cachedResponse
            }));
            return;
        }

        // Simulate processing payment
        let body = '';
        req.on('data', chunk => { body += chunk; });
        req.on('end', () => {
            const parsedBody = body ? JSON.parse(body) : {};
            const paymentResult = {
                transactionId: `tx_${Math.random().toString(36).substr(2, 9)}`,
                amount: parsedBody.amount || 100,
                status: "Success",
                timestamp: new Date().toISOString()
            };

            // Cache the result with the key
            processedRequests.set(idempotencyKey, paymentResult);

            res.writeHead(201);
            res.end(JSON.stringify({
                message: "Payment processed successfully (First attempt).",
                idempotentKey: idempotencyKey,
                result: paymentResult
            }));
        });
    }

    // Route 5: Catch-All 404
    else {
        res.writeHead(404);
        res.end(JSON.stringify({
            error: "Resource Not Found",
            statusCode: 404
        }));
    }
});

server.listen(PORT, () => {
    console.log(`\n🌐 HTTP Server running at \x1b[36mhttp://localhost:${PORT}\x1b[0m`);
    console.log(`   Interactive Lab endpoints active. Ctrl+C to terminate.`);
});
