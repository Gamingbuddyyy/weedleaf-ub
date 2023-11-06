import asyncio
import importlib
from pyrogram import idle
from AltSpam import app
from config import HELPABLE
from AltSpam.Plugins import ALL_MODULES
from AltSpam.logging import LOGGER
from AltSpam.Helpers import userbot, one, two


loop = asyncio.get_event_loop()


async def init(): 
    await app.start()

    for all_module in ALL_MODULES:
        imported_module = importlib.import_module("AltSpam.Plugins." + all_module)
        
        if (hasattr(imported_module, "__NAME__") and imported_module.__NAME__):
            imported_module.__NAME__ = imported_module.__NAME__
            
            if (hasattr(imported_module, "__HELP__") and imported_module.__HELP__):
                HELPABLE[imported_module.__NAME__.lower()] = imported_module
                
    LOGGER("AltSpam").info("Necessary Modules Imported Successfully !")
    
    await userbot()
    LOGGER("AltSpam").info(" ™°‌ 🇼𝔼𝔼𝔻𝕃𝔼𝔸𝔽 Started Successfully !")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("Sirion").info("Stopping  Bot !")
