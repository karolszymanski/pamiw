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
