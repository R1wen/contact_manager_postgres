const API_URL = "http://localhost:5000/contacts";
let contactEnCours = null;
let codesPaysGlobal = [];

window.onload = async function () {
  chargerContacts();
  const response = await fetch("CountryCodes.json");
  codesPaysGlobal = await response.json();

  const select = document.getElementById("country");
  for (let country of codesPaysGlobal) {
      const option = document.createElement("option");
      option.value = country.dial_code;
      option.textContent = `${country.name} (${country.dial_code})`;
      select.appendChild(option);
  }
};

function parseNumero(telephone) {
  let codePays = "";
  let numeroLocal = "";

  for (let country of codesPaysGlobal) {
    if (telephone.startsWith(country.dial_code)) {
      codePays = country.dial_code;
      numeroLocal = telephone.substring(country.dial_code.length).trim();
      break;
    }
  }

  return { codePays, numeroLocal };
}

function supprimerContact(id) {
  fetch(`${API_URL}/${id}`, {
    method: "DELETE",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ id }),
  })
    .then((res) => res.json())
    .then(() => {
      location.reload();
    });
}

function modifierContact(id) {
  fetch(`${API_URL}/${id}`)
    .then((res) => res.json())
    .then((contact) => {
      contactEnCours = contact;
      ouvrirModalModification(contact);
    })
    .catch((error) => {
      console.error("Erreur lors de la récupération du contact:", error);
      alert("Erreur lors de la récupération des données du contact");
    });
}

function ouvrirModalModification(contact) {
  document.getElementById("editNom").value = contact.nom;
  document.getElementById("editPrenom").value = contact.prenom;

  const { codePays, numeroLocal } = parseNumero(contact.telephone);

  document.getElementById("editCountry").value = codePays;
  document.getElementById("editLocalNumber").value = numeroLocal;

  document.getElementById("editModal").classList.remove("hidden");
}

function fermerModal() {
  document.getElementById("editModal").classList.add("hidden");
  contactEnCours = null;
}

function chargerContacts() {
  document.querySelector("tbody").innerHTML = "";
  fetch(API_URL)
    .then((res) => res.json())
    .then((data) => {
      data.forEach((contact) => {
        const id = contact.id;
        const nom = contact.nom;
        const prenom = contact.prenom;
        const telephone = contact.telephone;

        const tbody = document.querySelector("tbody");
        const tr = document.createElement("tr");
        tr.innerHTML = `
    <td class="border px-4 py-2">${nom}</td>
    <td class="border px-4 py-2">${prenom}</td>
    <td class="border px-4 py-2">${telephone}</td>
    <td onclick="modifierContact(${id})" class="border px-4 py-2 text-blue-500 cursor-pointer">Modifier</td>
    <td onclick="supprimerContact(${id})" class="border px-4 py-2 text-red-500 cursor-pointer">Supprimer</td>
  `;
        tbody.appendChild(tr);
      });
    });
}

document.getElementById("contactForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const nom = document.getElementById("nom").value.trim();
  const prenom = document.getElementById("prenom").value.trim();
  const countryCode = document.getElementById("country").value;
  const localNumber = document.getElementById("localNumber").value.trim();

  if (!countryCode) {
    alert("Veuillez choisir un pays");
    return;
  }

  const telephone = `${countryCode} ${localNumber}`;

  fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ nom, prenom, telephone }),
  })
    .then((res) => res.json())
    .then(() => {
      this.reset();
      location.reload();
    });
});

document.getElementById("editForm").addEventListener("submit", function (e) {
  e.preventDefault();

  if (!contactEnCours) {
    alert("Erreur: aucun contact sélectionné");
    return;
  }

  const nom = document.getElementById("editNom").value.trim();
  const prenom = document.getElementById("editPrenom").value.trim();
  const countryCode = document.getElementById("editCountry").value;
  const localNumber = document.getElementById("editLocalNumber").value.trim();

  if (!countryCode) {
    alert("Veuillez choisir un pays");
    return;
  }

  const telephone = `${countryCode} ${localNumber}`;

  fetch(`${API_URL}/${contactEnCours.id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ nom, prenom, telephone }),
  })
    .then((res) => res.json())
    .then(() => {
      fermerModal();
      chargerContacts();
    })
    .catch((error) => {
      console.error("Erreur lors de la modification:", error);
      alert("Erreur lors de la modification du contact");
    });
});

document.getElementById("editModal").addEventListener("click", function (e) {
  if (e.target === this) {
    fermerModal();
  }
});
