/**
 * Lab 1: DNS Resolution CLI
 * 
 * This script queries authoritative DNS servers and resolves A, AAAA, MX, 
 * and TXT records for a given domain using Node.js's native `dns/promises` module.
 * 
 * Run: node 01-dns-lookup/dns-lookup.js <domain>
 * Example: node 01-dns-lookup/dns-lookup.js google.com
 */

const dns = require('dns').promises;

const domain = process.argv[2] || 'google.com';

async function performDNSLookup(domain) {
    console.log(`\n🔍 Performing DNS Lookup for: \x1b[36m${domain}\x1b[0m\n`);
    
    // 1. Resolve IPv4 Address (A Record)
    try {
        const addresses = await dns.resolve4(domain);
        console.log(`🟢 \x1b[1mA Records (IPv4):\x1b[0m`);
        addresses.forEach(ip => console.log(`   └─ ${ip}`));
    } catch (err) {
        console.log(`🔴 A Records: Failed (${err.code})`);
    }

    // 2. Resolve IPv6 Address (AAAA Record)
    try {
        const addresses = await dns.resolve6(domain);
        console.log(`\n🟢 \x1b[1mAAAA Records (IPv6):\x1b[0m`);
        addresses.forEach(ip => console.log(`   └─ ${ip}`));
    } catch (err) {
        console.log(`\n🟡 AAAA Records: None or Failed (${err.code})`);
    }

    // 3. Resolve Mail Servers (MX Record)
    try {
        const mxRecords = await dns.resolveMx(domain);
        console.log(`\n🟢 \x1b[1mMX Records (Mail Servers):\x1b[0m`);
        mxRecords.sort((a, b) => a.priority - b.priority).forEach(record => {
            console.log(`   └─ Priority: ${record.priority} | Server: ${record.exchange}`);
        });
    } catch (err) {
        console.log(`\n🟡 MX Records: None or Failed (${err.code})`);
    }

    // 4. Resolve TXT Records (Text metadata / SPF)
    try {
        const txtRecords = await dns.resolveTxt(domain);
        console.log(`\n🟢 \x1b[1mTXT Records (Verification & SPF):\x1b[0m`);
        txtRecords.forEach(record => console.log(`   └─ ${record.join(' ')}`));
    } catch (err) {
        console.log(`\n🟡 TXT Records: None or Failed (${err.code})`);
    }

    // 5. Query Name Servers (NS Record)
    try {
        const nsRecords = await dns.resolveNs(domain);
        console.log(`\n🟢 \x1b[1mNS Records (Authoritative Name Servers):\x1b[0m`);
        nsRecords.forEach(ns => console.log(`   └─ ${ns}`));
    } catch (err) {
        console.log(`\n🟡 NS Records: None or Failed (${err.code})`);
    }
    
    console.log('\n✨ DNS query complete.\n');
}

performDNSLookup(domain);
