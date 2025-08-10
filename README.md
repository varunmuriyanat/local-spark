Install the latest OpenJDK
```
sudo apt update
sudo apt install openjdk-17-jdk
```


append this to ~/.bashrc
```
export JAVA_HOME=$(dirname $(dirname $(readlink -f $(which java))))
export PATH=$JAVA_HOME/bin:$PATH
```


run code
`python example.py`
