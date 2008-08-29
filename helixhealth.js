<!-- Original:  Nicholas Lupien (smylex@aol.com) -->

<!-- This script and many more are available free online at -->
<!-- The JavaScript Source!! http://javascript.internet.com -->

<!-- Begin
var rand1 = 0;
var useRand = 0;

images = new Array;
images[1] = new Image();
images[1].src = "images/sidebar_images/3genpedigree.jpg";
images[2] = new Image();
images[2].src = "images/sidebar_images/CancerRisk.jpg";
images[3] = new Image();
images[3].src = "images/sidebar_images/GdadFatherSon.jpg";
images[4] = new Image();
images[4].src = "images/sidebar_images/what_is_helix.jpg";

function swapPic() {
var imgnum = images.length - 1;
do {
var randnum = Math.random();
rand1 = Math.round((imgnum - 1) * randnum) + 1;
} while (rand1 == useRand);
useRand = rand1;
document.randimg.src = images[useRand].src;
}
//  End -->
