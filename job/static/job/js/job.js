const API_URL = 'http://127.0.0.1:8000/api/public/jobs/'

function loadMoreJobs() {
    fetch(API_URL)
        .then((response) => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`)
            }

            return response.json()
        })
        .then((data) => {
            console.info('Total de vagas retornadas', data.count)
        });
}
