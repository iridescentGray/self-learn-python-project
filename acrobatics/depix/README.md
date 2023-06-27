# Depix

## introduce

Depix is a tool for recovering passwords from pixelized screenshots.


- Original project：https://github.com/beurtschipper/Depix

## use

### Used by pyenv virtualenv plugin

    pyenv virtualenv  3.10.9 depix
    pyenv activate depix
    python -m pip install --upgrade pip
    pip install git+https://github.com/beurtschipper/Depix
    cd acrobatics/depix/
   

### Run
    # get some help
    depix -h  

    execute below code in shell: 
    depix \
    -p ./example/sublime_screenshot_pixels_gimp.png \
    -s ./example/debruin_sublime_Linux_small.png \
    -o output.png


### uninstall

    pyenv virtualenv-delete depix
