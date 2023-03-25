class FSMControl {
    static getCookie(name: string): string | null {
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

    public static launchTask(task: string): Promise<boolean> {
        let request = this.createRequest(task, 'launch');
        return fetch(request)
            .then(response => response.status === 200)
    }

    public static abortTask(task: string): Promise<boolean> {
        let request = this.createRequest(task, 'abort');
        return fetch(request)
            .then(response => response.status === 200)
    }

    public static waitTask(task: string): Promise<boolean> {
        let request = this.createRequest(task, 'wait');
        return fetch(request)
            .then(response => response.status === 200)
    }

    public static resumeTask(task: string): Promise<boolean> {
        let request = this.createRequest(task, 'resume');
        return fetch(request)
            .then(response => response.status === 200)
    }

    private static createRequest(task: string, state: string) {
        const csrftoken = this.getCookie('csrftoken');

        return new Request('http://127.0.0.1:8000/csApp/' + task + '/' + state, {method: 'POST',
            body: '',
            headers: {"X-CSRFToken": csrftoken ?? ''}})
    }

}

export default FSMControl;