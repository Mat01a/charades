import { test, expect, chromium } from '@playwright/test'

test('testing chat interactions', async () => {
    const browser = await chromium.launch()

    const context1 = await browser.newContext()
    const context2 = await browser.newContext()

    let page1 = await context1.newPage()
    let page2 = await context2.newPage()

    await page1.goto('')
    await page1.locator('input[name=username]').fill('Test')
    await page1.getByRole('button', { name: 'Submit' }).click()

    await page1.locator('input[name=roomName]').fill('test')
    await page1.getByRole('button', { name: 'Connect' }).click()

    await page2.goto('')
    await page2.locator('input[name=username]').fill('Test2')
    await page2.getByRole('button', { name: 'Submit' }).click()

    await page2.locator('input[name=roomName]').fill('test')
    await page2.getByRole('button', { name: 'Connect' }).click()

    await page1.locator('input[name=chatInput]').fill("Lorem ipsum")
    await page1.getByRole('button', { name: 'Send' }).click()

    await expect(page2.locator('id=chat')).toHaveText('Test:Lorem ipsum')

})