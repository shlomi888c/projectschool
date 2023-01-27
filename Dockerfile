FROM python:3.8-slim-buster

# Update the package list
RUN  apt-get update -y
RUN apt-get update && apt-get install -y \
curl

RUN apt install wget -y
RUN  wget https://packages.chef.io/files/stable/chef-workstation/21.10.640/ubuntu/20.04/chef-workstation_21.10.640-1_amd64.deb
RUN  dpkg -i chef-workstation_21.10.640-1_amd64.deb
RUN  apt install -y git
RUN  git clone https://shlomi888c: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@github.com/shlomi888c/chef-files-.git
RUN  mkdir etc/chef
RUN  mv chef-files-/* etc/chef
RUN  rm -r -f chef-files-/
EXPOSE 5000
RUN chef-client -o 'recipe[flaskapp]' --chef-license accept
ENTRYPOINT [ "python3" ]

# Run the command to start the Flask application
CMD ["home/projectschool/flask_app.py"]
