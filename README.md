# EtheronAuth [Prototype]

![IMG of Setup](https://github.com/Lebski/Etheronauth/blob/master/OAuth%20Eth2.jpg)

# Project Title

This project is part of my master-thesis about authorization of microservices on blockchains. 

## Getting Started

You need at least one verifier-script and one running EtheronAuthAPI-script. Also provide any web3 interface, e.g. geth. 
Please provide a matching public and private key pair and store it in the `/App/tokenstore.json` File.
And please run your scripts from the "App"-Folder. Had no time to adjust that. 

### Prerequisites

* [geth](https://github.com/ethereum/go-ethereum/wiki/geth) - Any ethereum node, providing web3
* [Ganache-cli](https://github.com/trufflesuite/ganache-cli) - ganache-cli for testing
* Python3 with web3, flask

### Installing

First you need to include your app folder in PYTHONPATH to use the etheronath package. 
Then deploy the contract to your desired network. 

```
export PYTHONPATH=$PYTHONPATH:$PWD  
echo $PYTHONPATH
python3 deploy.py
```

For the verifier run

```
python3 verifier/verifiy.py
```

For the API run

```
python3 etheronauthAPI.py
```


End with an example of getting some data out of the system or using it for a little demo


## Contributing

Please text me on [LinkedIn](https://www.linkedin.com/in/felix-leber-b1481699/), [twitter](https://twitter.com/_Lebsky) or whatever if you want to contibute to this project. 

## License

This project has no license or anything. But it's part of my master-thesis, so don't screw me. Please.
