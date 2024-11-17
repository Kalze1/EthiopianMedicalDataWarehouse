from telethon import TelegramClient
import os

# Telegram API credentials (Replace with your own)
API_ID = '26815993'
API_HASH = 'e8fe32bae8ed0fb6cd53ab5239bf36b3'
SESSION_NAME = 'data_from_Chemed_Telegram_Channel,'

# Target Telegram channel
TARGET_CHANNEL = 'https://t.me/lobelia4cosmetics'

# Directory to save images
IMAGE_DIR = 'scraped_images'
os.makedirs(IMAGE_DIR, exist_ok=True)

async def scrape_images(client, channel):
    """Scrape images from a Telegram channel."""
    try:
        # Connect to the channel
        print(f"Connecting to channel: {channel}")
        async for message in client.iter_messages(channel, limit=200):
            if message.photo:  # Check if the message contains a photo
                print(f"Downloading image from message ID: {message.id}")
                await client.download_media(message.photo, file=IMAGE_DIR)
    except Exception as e:
        print(f"Error scraping images: {e}")

def main():
    """Main function to initiate the scraping."""
    client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

    # Connect and scrape images
    with client:
        client.loop.run_until_complete(scrape_images(client, TARGET_CHANNEL))

if __name__ == "__main__":
    main()
