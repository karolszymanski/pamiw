let counter = 0;

function makeMeAdmin() {
	counter++
	if( counter >= 7) {
		counter = 0;
		toggleAdminMode(true)
	} else {
		toggleAdminMode(false)
	}
}

function toggleAdminMode(modeOn) {
	modeOn
		? document.getElementById('secret-function-content').style.display = 'unset'
		: document.getElementById('secret-function-content').style.display = 'none';
	document.getElementById('secret-function').value = modeOn;
}
