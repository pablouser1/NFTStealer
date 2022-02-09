from nftstealer.Stealer import Stealer

if __name__ == '__main__':
    stealer = Stealer()
    print("Getting NFT...")
    link = stealer.randomLink()
    if link:
        nft = stealer.getNft(link)
        if nft.id:
            filename = f'./nfts/{nft.id}.png'
            with open(filename, 'wb') as f:
                f.write(nft.data)
