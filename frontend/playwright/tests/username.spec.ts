import { test, expect } from '@playwright/test'


test('input username', async ({ page}) => {
    await page.goto('')

    await page.locator('input[name=username]').fill('Test')

    await page.getByRole('button', { name: 'Submit' }).click()
    
    await expect(page.getByRole('heading', { level: 1})).toHaveText("Puns game: Test")
})

