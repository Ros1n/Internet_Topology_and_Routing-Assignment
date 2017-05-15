@echo off
echo DATE: %DATE% AND TIME: %TIME%
tracert -4 www.columbia.edu
tracert -4 www.manit.ac.in
tracert -4 www.kyoto-u.ac.jp
tracert -4 www.epfl.ch
tracert -4 www.tu-berlin.de
tracert -4 www.nsu.ru
tracert -4 www.unsw.edu.au
echo traceroute finish.
echo END TIME: %TIME%
pause