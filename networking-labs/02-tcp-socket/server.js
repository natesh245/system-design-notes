/**
 * Lab 2: TCP Server
 * 
 * This file creates a native TCP socket server listening on port 8080.
 * It demonstrates stream-based connection handling, buffering, and closing states.
 * 
 * Run: node 02-tcp-socket/server.js
 */

const net = require('net');

const PORT = 8080;

const server = net.createServer((socket) => {
    const clientAddress = `${socket.remoteAddress}:${socket.remotePort}`;
    console.log(`\n🤝 \x1b[32mClient connected:\x1b[0m ${clientAddress}`);
    
    // Send initial greeting (handshake finished, connection established)
    socket.write('Welcome to the Low-Level TCP Stream Server!\n');
    socket.write(`Connected from: ${clientAddress}\n`);
    socket.write('Stream active. I will send you timestamps every second. Send "exit" to terminate.\n\n');

    // Send interval timestamps to stream data
    const intervalId = setInterval(() => {
        if (!socket.destroyed) {
            socket.write(`[SERVER TIMESTAMP]: ${new Date().toISOString()}\n`);
        }
    }, 1000);

    // Listen for incoming data from the client socket
    socket.on('data', (data) => {
        const message = data.toString().trim();
        console.log(`📩 [Client ${clientAddress}]: ${message}`);

        if (message.toLowerCase() === 'exit') {
            socket.write('Goodbye!\n');
            socket.end(); // Initiates standard TCP connection teardown
        } else {
            // Echo back the received message
            socket.write(`[ECHO]: Received "${message}"\n`);
        }
    });

    // Handle client connection closing
    socket.on('end', () => {
        console.log(`🛑 \x1b[33mClient disconnected (FIN received):\x1b[0m ${clientAddress}`);
        clearInterval(intervalId);
    });

    // Handle connection errors
    socket.on('error', (err) => {
        console.error(`💥 Socket error: ${err.message}`);
        clearInterval(intervalId);
    });
});

server.listen(PORT, () => {
    console.log(`\n🖥️  TCP Socket Server listening on \x1b[36mport ${PORT}\x1b[0m`);
    console.log(`   Waiting for connections (Run node 02-tcp-socket/client.js in a separate terminal)...`);
});
