import pyautogui as pa

sc=pa.screenshot(
  region=(100,100,100,100)
)
sc.save('./screenshots/hani.png')