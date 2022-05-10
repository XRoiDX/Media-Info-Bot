echo "Cloning Repo...."
if [ -z $BRANCH ]
then
  echo "Cloning main branch...."
  git clone https://github.com/XRoiDX/Media-Info-Bot /Media-Info-Bot
else
  echo "Cloning $BRANCH branch...."
  git clone https://github.com/XRoiDX/Media-Info-Bot -b $BRANCH /Media-Info-Bot
fi
cd /Media-Info-Bot
pip3 install -U -r requirements.txt
echo "Starting Bot.... By @XRoiDX"
python3 media.py
