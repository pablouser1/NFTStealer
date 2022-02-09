from nftstealer.Stealer import Stealer
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()
    stealer = Stealer()
    print("Getting NFT...")
    link = stealer.randomLink()
    if link:
        nft = stealer.getNft(link)
        if nft.id:
            filename = f'./nfts/{nft.id}.png'
            with open(filename, 'wb') as f:
                f.write(nft.data)
