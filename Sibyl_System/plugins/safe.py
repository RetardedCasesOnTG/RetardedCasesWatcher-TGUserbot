from Sibyl_System import System, system_cmd
import os
import sys
import subprocess


@System.on(system_cmd(pattern=r"ssc update"))
async def gitpull(event):
    subprocess.Popen("git pull", stdout=subprocess.PIPE, shell=True)
    await event.reply("Source code probably updated, restarting...")
    os.system("restart.bat")
    os.execv("start.bat", sys.argv)


@System.on(system_cmd(pattern=r"ssc reboot"))
async def reboot(event):
    if event.fwd_from:
        return
    await event.reply("Restarting.....")
    await System.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)


@System.on(system_cmd(pattern=r"ssc shutdown"))
async def shutdown(event):
    if event.fwd_from:
        return
    await event.reply("Shutting down... (Please manually start me if you need me.)")
    await System.disconnect()
