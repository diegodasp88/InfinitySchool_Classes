// Open modal
document.getElementById("openModalBtn").addEventListener("click", function () {
  document.getElementById("addTrackModal").style.display = "flex";
});

// Close modal
document.getElementById("closeModalBtn").addEventListener("click", function () {
  document.getElementById("addTrackModal").style.display = "none";
});

// Close modal when clicking outside of modal content
window.addEventListener("click", function (event) {
  if (event.target === document.getElementById("addTrackModal")) {
    document.getElementById("addTrackModal").style.display = "none";
  }
});

async function loadTracks() {
    const url = "https://68d32aefcc7017eec5462590.mockapi.io/music"
    const response = await fetch(url)
    const tracks = await response.json()

    const tbody = document.querySelector("tbody")
    tbody.innerHTML = "" // limpar conteúdo antes de inserir novas músicas

    tracks.forEach(track => {
        const trackHtmlStructure = `
            <tr>
                <td>${track.id}</td>
                <td class="faixa">
                    <img src="${track.imagem}" alt=""/>
                    <div>${track.nome}</div>
                </td>
                <td>${track.streams}</td>
                <td>${track.duracao}</td>
                <td><a href="#" class="play-button">▶</a></td>
                <td>
                    <button 
                        class="delete-button" 
                        onclick="deleteTrack(${track.id})">
                            Excluir
                    </button>
                </td> 
            </tr>

        `
        tbody.innerHTML += trackHtmlStructure
    });
}
loadTracks()

async function addTrack() {
    const trackName = document.querySelector("#trackName").value
    const trackDuration = document.querySelector("#trackDuration").value
    const trackStreams = document.querySelector("#trackStreams").value
    const trackImage = document.querySelector("#trackImage").value

    const track = {
        nome: trackName,
        duracao: trackDuration,
        streams: trackStreams,
        imagem: trackImage
    };

    const url = "https://68d32aefcc7017eec5462590.mockapi.io/music"
    const response = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(track)
    })

    loadTracks()
    fecharFormulario();
}

async function deleteTrack(id) {
    const url = `https://68d32aefcc7017eec5462590.mockapi.io/music/${id}`
    const response = await fetch(url, { method: "DELETE" })

    if (response.status === 200) {
        alert("Música excluída com sucesso!")
        loadTracks()
    } else {
        alert("Erro ao excluir música.")
    }
}