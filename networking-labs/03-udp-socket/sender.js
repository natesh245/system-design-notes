/**
 * Lab 3: UDP Sender (Client)
 * 
 * Sends a sequence of fire-and-forget datagram packets to localhost:9090.
 * Highlights the zero-handshake startup speed of UDP.
 * 
 * Run: node 03-udp-socket/sender.js
 */

const dgram = require('dgram');

const PORT = 9090;
const HOST = '127.0.0.1';

const client = dgram.createSocket('udp4');

const packets = [
    "Packet #1: Hello from the UDP sender!",
    "Packet #2: Video frame slice #231",
    "Packet #3: Audio packet slice #112",
    "Packet #4: Realtime location update: x: 10, y: 45",
    "Packet #5: Last packet (fire-and-forget complete)."
];

console.log(`\n🚀 Starting UDP Packet Sender...`);

packets.forEach((msg, idx) => {
    // Send packets sequentially with a small delay
    setTimeout(() => {
        const messageBuffer = Buffer.from(msg);
        
        console.log(`✉️  Sending: "${msg}"`);
        
        client.send(messageBuffer, 0, messageBuffer.length, PORT, HOST, (err) => {
            if (err) {
                console.error(`💥 Error sending packet #${idx + 1}: ${err.message}`);
            }
            
            // Close socket after the last packet
            if (idx === packets.length - 1) {
                console.log(`\n✅ All packets sent. Closing socket.\n`);
                client.close();
            }
        });
    }, idx * 500); // 500ms delay between packets
});
