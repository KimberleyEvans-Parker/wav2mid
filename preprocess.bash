# 19 Sep 2018
# By: Aldrian Obaja Muis
# To run preprocess.py on partial datasets

basedir="../MAPS"
# Do everything in one go (might have memory error)
python preprocess.py baseline ${basedir}

# Do in parts (doesn't work yet with the training code)
#for subdir in $(ls ${basedir}); do
#    if [ ! -d ${basedir}/${subdir} ]; then
#        continue
#    fi
#    echo ${basedir}/${subdir}
#    for subsubdir in $(ls ${basedir}/${subdir}); do
#        python preprocess.py baseline ${basedir}/${subdir}/${subsubdir}
#    done
#done
