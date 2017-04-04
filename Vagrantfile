Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.provider "virtualbox" do |vb|
    vb.memory = 1024
  end

  config.vm.provision "shell", inline: <<-SHELL
    apt -y update
    apt install -y python-minimal
  SHELL
end
