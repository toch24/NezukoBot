from selenium import webdriver
from time import sleep
import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='!')

#url links
protect_url = "https://www.amazon.com/Trojan-BARESKIN-Condoms-specially-designed/dp/B097YLRH21/ref=sr_1_2?dchild=1&keywords=condom&qid=1621456735&sr=8-2&th=1"
rtx1a = "https://www.amazon.com/MSI-GeForce-RTX-3060-12G/dp/B08WPRMVWB/ref=mp_s_a_1_3?dchild=1&keywords=rtx+3060&qid=1621534999&sr=8-3"
rtx2a = "https://www.amazon.com/ASUS-Graphics-DisplayPort-Military-Grade-Certification/dp/B08WHJPBFX/ref=mp_s_a_1_9?dchild=1&keywords=rtx+3060&qid=1621535552&sr=8-9"
rtx1n = "https://www.newegg.com/evga-geforce-rtx-3060-12g-p5-3657-kr/p/N82E16814487539?Description=rtx3060&cm_re=rtx3060-_-14-487-539-_-Product"
rtx2n = "https://www.newegg.com/gigabyte-geforce-rtx-3060-gv-n3060gaming-oc-12gd/p/N82E16814932402?Description=rtx3060&cm_re=rtx3060-_-14-932-402-_-Product"
rtx3n = "https://www.newegg.com/msi-geforce-rtx-3060-rtx-3060-ventus-2x-12g-oc/p/N82E16814137632?Description=rtx3060&cm_re=rtx3060-_-14-137-632-_-Product"
rtx4n = "https://www.newegg.com/msi-geforce-rtx-3060-rtx-3060-gaming-x-12g/p/N82E16814137630?Description=rtx3060&cm_re=rtx3060-_-14-137-630-_-Product"
rtx5n = "https://www.newegg.com/asus-geforce-rtx-3060-rog-strix-rtx3060-o12g-gaming/p/N82E16814126492?Description=rtx3060&cm_re=rtx3060-_-14-126-492-_-Product"
rtx6n = "https://www.newegg.com/gigabyte-geforce-rtx-3060-gv-n3060aorus-e-12gd/p/N82E16814932400?Description=rtx3060&cm_re=rtx3060-_-14-932-400-_-Product"
rtx7n = "https://www.newegg.com/gigabyte-geforce-rtx-3060-gv-n3060eagle-12gd/p/N82E16814932399?Description=rtx3060&cm_re=rtx3060-_-14-932-399-_-Product"
rtx8n = "https://www.newegg.com/asus-geforce-rtx-3060-dual-rtx3060-12g/p/N82E16814126493?Description=rtx3060&cm_re=rtx3060-_-14-126-493-_-Product"
rtx9n = "https://www.newegg.com/zotac-geforce-rtx-3060-zt-a30600e-10m/p/N82E16814500509?Description=rtx3060&cm_re=rtx3060-_-14-500-509-_-Product"
rtx10n = "https://www.newegg.com/gigabyte-geforce-rtx-3060-gv-n3060eagle-oc-12gd/p/N82E16814932403?Description=rtx3060&cm_re=rtx3060-_-14-932-403-_-Product"

#Check links commands
@bot.command()
async def rtx3060(ctx):
    check = checkBot()
    amazonurls = [rtx1a, rtx2a]
    neweggurls = [rtx1n, rtx2n, rtx3n, rtx4n, rtx4n, rtx5n, rtx6n, rtx7n, rtx8n, rtx9n, rtx10n]
    #checking for amazon urls
    checkurl = check.amazon(amazonurls)
    #checking for newegg urls
    checkurl = check.newegg(neweggurls)
    if checkurl != " ":
        await ctx.send("RTX 3060 available! " + checkurl)
    else:
        await ctx.send("Sorry no RTX 3060 available yet :(")

@bot.command()
async def protect(ctx):
    check = checkBot()
    urls = [protect_url]
    checkurl = check.amazon(urls)
    if checkurl != " ":
        await ctx.send("Remember to always protect yourself! " + checkurl)
    else:
        await ctx.send("I am stupid sorry")
    

#Roleplaying commands
@bot.command()
async def joke(ctx):
    jokes = ['Knock knock who is there? \n ur mom', 'I only know 25 letters of the alphabet. I dont know y.', 'Where do fruits go on vacation? Pear-is!'
            , 'How do you make 7 even? Take away the s.']
    await ctx.send(random.choice(jokes))

@bot.command()
async def arigato(ctx):
    await ctx.send("nya")


#Where the magic happens
class checkBot():
    def __init__(self):
        options = webdriver.ChromeOptions()
        #options.add_argument('--headless')

        self.driver = webdriver.Chrome(chrome_options = options)

    #checking for amazon links
    def amazon(self, urls = []):
        count = 0
        for url in urls:
            count += 1
            self.driver.get(url)
            try:
                addCart = self.driver.find_element_by_xpath('//*[@id="add-to-cart-button"]')
                addCart.click()
                print("Add to cart button found!")
                return url

            except Exception as e:
                print("No add to cart button found")
                if count == len(urls):
                    return " "

    #checking for newegg links
    def newegg(self, urls = []):
        count = 0
        for url in urls:
            count += 1
            self.driver.get(url)
            try:
                addCart = self.driver.find_element_by_xpath('//*[@class="btn btn-primary btn-wide"]')
                addCart.click()
                print("Add to cart button found!")
                return url

            except Exception as e:
                print("No add to cart button found")
                if count == len(urls):
                    return " "

if __name__ == '__main__':
    #run the discord bot
    print("Now running the Nezuko bot")
    bot.run('ODQ0MzM4MTEwMDM5ODUxMDU4.YKQ9JA.7HGf0o9GkWpBcm1zEMRFHxsUbmI')