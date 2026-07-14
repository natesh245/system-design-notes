/**
 * Lab 3: UDP Receiver (Server)
 * 
 * Creates a socket that listens for incoming UDP packets on port 9090.
 * Demonstrates connectionless, packet-boundary-based (datagram) transmission.
 * 
 * Run: node 03-udp-socket/receiver.js
 */

const dgram = require('dgram');

const PORT = 9090;
const HOST = '127.0.0.1';

const socket = dgram.createSocket('udp4');

socket.on('listening', () => {
    const address = socket.address();
    console.log(`\n📡 UDP Receiver listening on \x1b[36m${address.address}:${address.port}\x1b[0m`);
    console.log(`   Waiting for packets... (Run node 03-udp-socket/sender.js)`);
});

socket.on('message', (msg, rinfo) => {
    console.log(`📦 [Packet from ${rinfo.address}:${rinfo.port}] (Size: ${rinfo.size} bytes):`);
    console.log(`   └─ Content: "\x1b[32m${msg.toString().trim()}\x1b[0m"`);
});

socket.on('error', (err) => {
    console.error(`💥 Socket error: ${err.message}`);
    socket.close();
});

socket.bind(PORT, HOST);
