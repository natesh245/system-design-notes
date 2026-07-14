/**
 * Lab 2: TCP Client
 * 
 * This script connects to the TCP socket server on port 8080 and
 * hooks standard input to send text messages over the network stream.
 * 
 * Run: node 02-tcp-socket/client.js
 */

const net = require('net');

const HOST = '127.0.0.1';
const PORT = 8080;

const client = net.createConnection({ host: HOST, port: PORT }, () => {
    console.log(`\n✅ \x1b[32mSuccessfully connected to TCP server at ${HOST}:${PORT}\x1b[0m`);
    console.log(`   Type messages in this terminal. Type "exit" to quit.\n`);
});

// Handle incoming stream chunks from server
client.on('data', (data) => {
    console.log(data.toString());
});

// Handle connection closure
client.on('end', () => {
    console.log('\n🛑 Connection terminated by server.');
    process.exit(0);
});

// Handle connection error
client.on('error', (err) => {
    console.error(`\n💥 Connection error: ${err.message}`);
    process.exit(1);
});

// Listen to terminal input and send to server
process.stdin.on('data', (input) => {
    client.write(input);
});
