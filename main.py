#Get libs
import dearpygui.dearpygui as dpg
import dearpygui.logger as dpg_logger
from pytube import YouTube

#make globals
logger = dpg_logger.mvLogger()
#downloader window
def downloader_window():
    with dpg.window(label="Downloader", width=400, height=20):
        url_box_id = dpg.add_input_text(id=69, label="Enter YouTube URL", default_value="Youtube.com")
        #dpg.add_edited_handler(url_box_id, callback=get_url)
        dpg.add_button(label="Download", callback=download_vid)

def finished():
    print("Hello")

#converter
def download_vid():
    vid_url = dpg.get_value(69)
    print(type(vid_url))

    
    #putube stuff
    my_video = YouTube(vid_url)
    
    my_video = my_video.streams.get_highest_resolution()
    logger.log("Video Downloaded!, please wait a few seconds \n while the video is processed (time depends on video length).")
    my_video.download("")
    
def info():
    logger.log_info("This is a logger made by Hugo Boston\nI used Dear pygui and pytube.")

#menu bar
with dpg.viewport_menu_bar():
     with dpg.menu(label="Window"):
        dpg.add_menu_item(label="Downloader", callback=downloader_window)
     with dpg.menu(label="About"):
        dpg.add_menu_item(label="Info", callback=info)
        dpg.add_menu_item(label="Dear PyGui", callback=dpg.show_about)
        


#main program

downloader_window()
logger.log_info("Welcome to my YouTube Video downloader\nPaste link into bar and click Download to use.")
dpg.start_dearpygui()