from Sibyl_System import System, system_cmd, make_collections, INSPECTORS, ENFORCERS
from Sibyl_System.strings import on_string
from Sibyl_System.plugins.Mongo_DB.gbans import get_gbans 
import logging
import importlib
import asyncio
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

from Sibyl_System.plugins import to_load

HELP = {}
IMPORTED = {}

for load in to_load:
    imported = importlib.import_module("Sibyl_System.plugins." + load)
    if not hasattr(imported, "__plugin_name__"):
        imported.__plugin_name__ = imported.__name__

    if not imported.__plugin_name__.lower() in IMPORTED:
        IMPORTED[imported.__plugin_name__.lower()] = imported

    if hasattr(imported, "help_plus") and imported.help_plus:
        HELP[imported.__plugin_name__.lower()] = imported

@System.on(system_cmd(pattern=r'status', allow_enforcer = True))
async def status(event):
  msg = await event.reply('Portable Psychological Diagnosis and Suppression System.')
  time.sleep(1)
  await msg.edit('Initialising ▫️◾️▫️') 
  time.sleep(1)
  await msg.edit('Initialising ◾️▫️◾️')
  time.sleep(1)
  await msg.edit('Initialising ▫️◾️▫️')
  time.sleep(1)
  await msg.edit('Initialising ◾️▫️◾️')
  time.sleep(1)
  await msg.edit('Initialising ▫️◾️▫️')
  time.sleep(1)
  await msg.edit('Initialising ◾️▫️◾️')
  time.sleep(1)
  await msg.edit('Initialising ▫️◾️▫️')
  time.sleep(1)
  await msg.edit('Connection successful!')
  time.sleep(2)  
  sender = await event.get_sender()
  user_status = 'Inspector' if sender.id in INSPECTORS else 'Enforcer'
  time.sleep(1)
  await msg.edit(on_string.format(Enforcer = user_status, name=sender.first_name))

@System.on(system_cmd(pattern='ssc stats'))
async def stats(event):
  msg = f"Processed {System.processed} messages since last restart."
  msg += f"\n{len((await get_gbans())['victim'])} users are gbanned."
  msg += f"\n{len(ENFORCERS)} Enforcers & {len(INSPECTORS)} Inspectors"
  g = 0
  async for d in event.client.iter_dialogs(limit=None):
        if d.is_channel and not d.entity.broadcast:
            g += 1
        elif d.is_group:
            g += 1
  msg += f"\nModerating {g} Groups"
  await event.reply(msg)

@System.on(system_cmd(pattern=r'help', allow_slash=False, allow_inspectors = True))
async def send_help(event):
         try:
            help_for = event.text.split(" ", 1)[1].lower()
         except IndexError:
            msg = "**Currently available plugins with help**\n\n"
            for x in HELP.keys():
                msg += f"`{x.capitalize()}`\n"
            await event.reply(msg)
            return
         if help_for in HELP:
              await event.reply(HELP[help_for].help_plus)
         else:
              return


async def main():
  await make_collections()
  await System.start()
  await System.catch_up()
  await System.run_until_disconnected()

if __name__ == '__main__':
  asyncio.get_event_loop().run_until_complete(main())
