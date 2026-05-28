============================
  CAT CATCH BOT - SETUP GUIDE
============================

WHAT YOU NEED
-------------
- A PC with Python installed
- Your Discord account token
- The channel ID where Cat Bot spawns cats

------------------------------------------------------------
STEP 1: INSTALL PYTHON
------------------------------------------------------------
1. Go to https://www.python.org/downloads/
2. Download the latest version (3.10 or newer)
3. Run the installer
   - IMPORTANT: Check the box that says "Add Python to PATH" before clicking Install

------------------------------------------------------------
STEP 2: INSTALL THE REQUIRED LIBRARY
------------------------------------------------------------
1. Open Command Prompt (press Windows key, type "cmd", hit Enter)
2. Type this and press Enter:

   pip install discord.py-self

   Wait for it to finish. You should see "Successfully installed..."

------------------------------------------------------------
STEP 3: GET YOUR DISCORD TOKEN
------------------------------------------------------------
WARNING: Your token is like your password. NEVER share it with anyone.

1. Open Discord in your browser (discord.com/app) — NOT the desktop app
2. Press F12 to open DevTools
3. Go to the "Network" tab
4. Press Ctrl+R to refresh the page
5. In the filter box, type "science"
6. Click on one of the results that appear
7. Click the "Headers" tab on the right
8. Scroll down to "Request Headers"
9. Find the line that starts with "Authorization:"
10. Copy the long string of letters/numbers after it — that's your token

------------------------------------------------------------
STEP 4: GET THE CHANNEL ID
------------------------------------------------------------
1. In Discord, go to Settings > Advanced > turn on "Developer Mode"
2. Right-click the cat-catch channel
3. Click "Copy Channel ID"
4. Paste it somewhere — you'll need it next

------------------------------------------------------------
STEP 5: CONFIGURE THE BOT
------------------------------------------------------------
1. Open the file "catbot_sniper.py" in Notepad (right-click > Open with > Notepad)
2. Find this line near the top:

   TOKEN = "UR DISCORD BOT TOKEN HERE DO NOT SHARE THIS WITH ANYONE"

   Replace the text inside the quotes with your actual token.

3. Find this line:

   CHANNEL_ID = 1491396576705384529

   Replace the number with your channel ID (no quotes around it).

4. Save the file (Ctrl+S)

------------------------------------------------------------
STEP 6: RUN THE BOT
------------------------------------------------------------
1. Open Command Prompt
2. Navigate to the folder where catbot_sniper.py is saved.
   Example:
   cd "C:\Users\YourName\Desktop\Cat Catch"

3. Type this and press Enter:

   python catbot_sniper.py

4. If it worked, you'll see:
   "Logged in as [your account] — Watching channel ID: ... — Sniping cats..."

To stop the bot, press Ctrl+C in the Command Prompt window.

------------------------------------------------------------
TROUBLESHOOTING
------------------------------------------------------------
"pip is not recognized"
  -> You didn't check "Add Python to PATH" during install.
     Uninstall Python and reinstall it, making sure to check that box.

"ModuleNotFoundError: No module named 'discord'"
  -> Run: pip install discord.py-self

"LoginFailure" or "Improper token"
  -> Your token is wrong or expired. Redo Step 3.

"python is not recognized"
  -> Same as the pip issue — reinstall Python with "Add to PATH" checked.
