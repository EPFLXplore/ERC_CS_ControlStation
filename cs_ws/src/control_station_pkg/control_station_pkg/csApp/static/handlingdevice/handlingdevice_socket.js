const tabName = JSON.parse(document.getElementById('tab-name').textContent);
		const chatSocket = new WebSocket(
			'ws://'
			+ window.location.host
			+ '/ws/csApp/'
			+ tabName
			+ '/'
		);

		chatSocket.onmessage = function (e) {

			const data = JSON.parse(e.data);

			/* display joint coordinates */
			let coordinates = document.querySelectorAll('#joint1_coord, #joint2_coord, #joint3_coord, #joint4_coord, #joint5_coord, #joint6_coord, #joint7_coord');
			let i = 0;
			coordinates.forEach(coord => {
				document.getElementById(coord.id).innerHTML = (Math.round((data.joint_pos[i] + Number.EPSILON) * 180 / Math.PI * 100) / 100);
				i += 1;
				
			})

			let sliders = document.querySelectorAll('#joint1_slider, #joint2_slider, #joint3_slider, #joint4_slider, #joint5_slider, #joint6_slider');
			let f = 0;
			sliders.forEach(slider => {
				document.getElementById(slider.id).value = (Math.round((data.joint_pos[f] + Number.EPSILON) * 180 / Math.PI * 100) / 100);
				f += 1;
			 })

			/* display ToF */
			document.getElementById('tof').innerHTML = Math.round((data.tof + Number.EPSILON) * 100) / 100000 //divide by 100000 to convert into meters


			let elements = document.querySelectorAll("td:not(.element-title)");
			let k = 0;
			elements.forEach(e => {
				e.innerHTML = data.detected_elems[k];
				//console.log(Math.round((data.detected_elems[k] + Number.EPSILON) * 100) / 100)
				
				k += 1;
			})

		};

		chatSocket.onclose = function (e) {
			console.log('Switched Tab');
		};


		/* WHEN SETTING A NEW ID */
		let dropdownList = document.getElementById('dropdown_id');
		//let setButton = document.getElementById('set')
		/*setButton.onclick = (v) => {
			console.log("Selected value is: " + dropdownList.value);
		}*/