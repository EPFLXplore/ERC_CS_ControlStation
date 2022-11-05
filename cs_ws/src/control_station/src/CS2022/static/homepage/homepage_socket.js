const tabName = JSON.parse(document.getElementById('tab-name').textContent);
		console.log(tabName)
		const chatSocket = new WebSocket(
			'ws://'
			+ window.location.host
			+ '/ws/CS2022/'
			+ tabName
			+ '/'
		);

		chatSocket.onmessage = function(e) {
			const data = JSON.parse(e.data);
			
			console.log("debug")


		};

		chatSocket.onclose = function(e) {
			console.error('Chat socket closed unexpectedly');
		};