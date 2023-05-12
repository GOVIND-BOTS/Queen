import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "13976276"))
    API_HASH = os.environ.get("API_HASH", "7f024cbc744a2f44569c3641b5ccecb7")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6052195748:AAFpuknQjZ9OOnqoTKoL2515BhhneWW_ZRI")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOK4Bu6W19gfF2Ig3sEVKwyUjifsCprEbCSVYJJKOCpM1NNvUnVlpS2axCrxXeC4MCsMfc0GRkaJ4M-FtVV75osIe_-SAIWldFiCIVLOY5m0SlA_0Cg2t_6euVAtyUNO2kbFPciNMNvRx_imPLmGwZsQ0aLllRJBDoMvXUkvoug1drIIqOonfwSYGcH6MPnu_Opy2i3WHIBR-cN0sFvYJSR_2iL_iHXo50KpGfBmMwTzCzVSCXENAx--0rnKmGU3fNcSa-LxOg3Mnz36hd1ntiRQdYK8LDqRoXNhbmbdU9KKqW6CHLO9Pn6bn3uD60M3QZpgb13lG9zWnBcX3aiwWNfUlV_k=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "ICC_ToXiC_MuSiC_BoT")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat", "https://t.me/indian_chatting_club_offical") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel", "https://t.me/tha_govind_op") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/b2258dbee2401c426eb3c.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5870880892")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
