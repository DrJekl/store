document.addEventListener("DOMContentLoaded", function () {
	let thumbs = document.querySelectorAll("#thumb");
	let pics = document.querySelectorAll("#pic");
	for (let i = 0; i < thumbs.length; i++) {
		thumbs[i].style.borderRadius = "5px";
		if (thumbs[i].width >= thumbs[i].height) {
			thumbs[i].width = 180;
		}
		else {
			thumbs[i].height = 180;
		}
	}
	for (let i = 0; i < pics.length; i++) {
		pics[i].style.borderRadius = "10px";
		while (pics[i].height > 640 || pics[i].width > 640) {
			pics[i].height = pics[i].height * 0.9;
			pics[i].width = pics[i].width * 0.9;
		}
	}
});