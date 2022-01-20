let counter = 0;

function makeMeAdmin() {
	counter++
	if( counter >= 7) {
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

function filterPackages() {
	const packages = document.getElementsByClassName('package-info-container')
	const query = document.getElementById('filter-packages-input').value.toLowerCase()
	for (let pack of packages) {
		const title = pack.querySelector('#package-title').innerText
		const packageId = pack.querySelector('#package-id').innerText
		if(!title.toLowerCase().match(query) && !packageId.toLowerCase().match(query)) {
			document.getElementById(`package-${packageId}`).style.display = 'none';
		} else {
			document.getElementById(`package-${packageId}`).style.display = 'block';
		}
	}
}
