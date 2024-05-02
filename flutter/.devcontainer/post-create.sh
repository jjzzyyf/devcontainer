# download flutter sdk
echo "Downloading flutter sdk..."
git clone https://github.com/flutter/flutter.git -b stable --depth 1 /usr/lib/flutter

# install dart sdk
apt-get update
apt-get install apt-transport-https
wget -qO- https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo gpg --dearmor -o /usr/share/keyrings/dart.gpg
echo 'deb [signed-by=/usr/share/keyrings/dart.gpg arch=amd64] https://storage.googleapis.com/download.dartlang.org/linux/debian stable main' | sudo tee /etc/apt/sources.list.d/dart_stable.list

apt-get update
apt-get install dart

# Check flutter doctor
# echo "Checking flutter doctor..."
# flutter doctor
