const puppeteer = require('puppeteer');

async function generateAccount() {
    const characters = 'abcdefghijklmnopqrstuvwxyz0123456789';
    const randomString = length => Array.from({ length }, () => characters[Math.floor(Math.random() * characters.length)]).join('');

    const randomText = length => Array.from({ length }, () => characters[Math.floor(Math.random() * 26)]).join('');

    const nickname = randomText(8);
    const password = randomString(12);
    const email = `${nickname}@${randomText(5)}.com`;

    const browser = await puppeteer.launch();
    const page = await browser.newPage();

    await page.goto('https://accounts.spotify.com/en/login?continue=https%3A%2F%2Fopen.spotify.com%2F');

    await page.waitForSelector('input[type="text"]');
    await page.type('input[type="text"]', email);

    await page.waitForSelector('input[type="password"]');
    await page.type('input[type="password"]', password);

    await page.click('button[data-testid="login-button"]');

    await page.waitForNavigation();

    await page.goto('https://open.spotify.com/');

    // Enter the playlist URL
    const playlistUrl = 'https://open.spotify.com/playlist/35DIHSa0QoEsc64WVRpvdB?si=54e66ad7b3d04f87';
    await page.goto(playlistUrl);

    await page.waitForSelector('button[title="Follow"]');
    await page.click('button[title="Follow"]');

    await page.goto('https://open.spotify.com/logout');

    await browser.close();

    return `${nickname}:${email}:${password}`;
}

async function main() {
    const numberOfAccounts = 1; // Set the number of accounts to generate
    const outputFilePath = 'accounts.txt'; // Set the output file path

    console.log(`Generating ${numberOfAccounts} account(s)`);

    const output = [];

    for (let i = 0; i < numberOfAccounts; i++) {
        const accountInfo = await generateAccount();
        output.push(accountInfo);
        console.log(accountInfo);
    }

    if (outputFilePath) {
        const fs = require('fs');
        fs.writeFileSync(outputFilePath, output.join('\n'));
        console.log(`Accounts saved to ${outputFilePath}`);
    }
}

main().catch(console.error);
