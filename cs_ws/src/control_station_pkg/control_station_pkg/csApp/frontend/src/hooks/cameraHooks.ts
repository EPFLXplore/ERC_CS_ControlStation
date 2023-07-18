import React from "react";
import { useState, useEffect } from "react";
import { Cameras } from "../utils/cameras.type";

function useCameraSelector(item: Cameras) {
	const [socket, setSocket] = useState<WebSocket | null>(null);
	const [image, setImage] = React.useState<string>("");

	const getCookie = (name: string): string | null => {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

	useEffect(() => {

		const csrftoken = getCookie('csrftoken');
		let formData = new FormData();
			formData.append("index",  item.toString());
			//formData.append('y',  y.toString());
			//formData.append('yaw', o.toString());

		let request = new Request("http://127.0.0.1:8000/csApp/cameras/enable_cameras",
			{
				method: "POST",
				headers: {
					"X-CSRFToken": csrftoken ?? ''
				},
				body: formData,
			})
	
		fetch(request).then((res) => res.json()).then((data) => console.log(data));

		let cameraSocket = new WebSocket(
			"ws://" + window.location.host + "/ws/cameras/" + "video" + item + "/"
		);

		cameraSocket.onmessage = (e) => {
			const data = JSON.parse(e.data);
			console.log(data.data);
			setImage(data.data);
		};

		cameraSocket.onerror = (e) => {
			console.log(e);
			setSocket(null);
		};

		setSocket(cameraSocket);
	}, []);

	return [image] as const;
}

export default useCameraSelector;
