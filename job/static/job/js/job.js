let currentApiUrl = '/api/public/jobs/'

function loadMoreJobs() {
    fetch(currentApiUrl)
        .then((response) => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`)
            }

            return response.json()
        })
        .then((data) => {
            removeProgressBar()
            createItems(data.results)
            currentApiUrl = data.next
        });
}

function createItems(jobs) {
    const ul = document.getElementById('jobList')
       
    jobs.forEach(job => {
        const li = createItem(job)
        ul.appendChild(li)
    });
}

function createItem(job) {
    const li = document.createElement('li')
    li.className = 'list-group-item'
    li.innerHTML = createItemHtml(job)
    return li
}

function createItemHtml(job) {
    return `\
    <div class="d-flex flex-column flex-sm-row"> \
        <div class="flex-fill d-flex"> \
            <div class="align-self-center pr-3"> \
                <i class="bi bi-pie-chart icon bg-secondary text-white rounded-circle"></i> \
            </div> \
            <div class="flex-fill pr-3"> \
                <p class="text-muted">${job.company.name}</p> \
                <h6 class="font-weight-bold">${job.title}</h6> \
                <small><i class="bi bi-geo-alt text-secondary pr-2"></i>${job.location}</small> \
            </div> \
        </div> \
        <div class="d-flex align-items-center"> \
            <a class="btn btn-primary w-100" href="${job.id}">Detalhes</a> \
        </div> \
    </div>`;
}

function removeProgressBar() {
    const element = document.getElementById('progressJobList')

    if (element) {
        element.remove()
    }
}

loadMoreJobs()
