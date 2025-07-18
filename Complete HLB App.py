<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>My Code Projects</title>
  <style>
    body {
      margin: 0;
      font-family: 'Segoe UI', sans-serif;
      background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
      color: #fff;
    }

    header {
      background-color: rgba(0, 0, 0, 0.4);
      padding: 1rem 2rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    header h1 {
      margin: 0;
    }

    .btn-new {
      background-color: #00bcd4;
      color: #fff;
      padding: 0.6rem 1.2rem;
      border: none;
      border-radius: 12px;
      cursor: pointer;
      font-weight: bold;
    }

    .container {
      padding: 2rem;
    }

    .projects-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1.5rem;
    }

    .project-card {
      background: rgba(255, 255, 255, 0.05);
      border-radius: 16px;
      padding: 1rem;
      box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
      text-align: center;
    }

    .project-card img {
      max-width: 100%;
      border-radius: 12px;
      margin-bottom: 1rem;
      max-height: 160px;
      object-fit: cover;
    }

    .project-card h2 {
      margin-top: 0;
      font-size: 1.2rem;
    }

    .project-card p {
      font-size: 0.9rem;
      color: #ddd;
    }

    .project-card a {
      display: inline-block;
      margin-top: 0.5rem;
      color: #00bcd4;
      text-decoration: none;
      font-size: 0.9rem;
    }

    .project-card .tags {
      margin-top: 0.5rem;
      display: flex;
      flex-wrap: wrap;
      gap: 5px;
      justify-content: center;
    }

    .tag {
      background-color: #0097a7;
      padding: 3px 8px;
      border-radius: 12px;
      font-size: 0.75rem;
    }

    footer {
      text-align: center;
      padding: 1rem;
      font-size: 0.8rem;
      background-color: rgba(0, 0, 0, 0.2);
    }

    /* Modal Styles */
    .modal {
      display: none;
      position: fixed;
      z-index: 999;
      left: 0; top: 0;
      width: 100%; height: 100%;
      background-color: rgba(0, 0, 0, 0.6);
      align-items: center;
      justify-content: center;
    }

    .modal-content {
      background-color: #1e1e2f;
      padding: 2rem;
      border-radius: 20px;
      width: 90%;
      max-width: 450px;
    }

    .modal-content h3 {
      margin-top: 0;
      color: #00bcd4;
    }

    .modal-content input, .modal-content textarea {
      width: 100%;
      padding: 0.6rem;
      margin-bottom: 1rem;
      border-radius: 8px;
      border: none;
      background-color: #333;
      color: #fff;
    }

    .modal-content input[type="file"] {
      padding: 0.4rem;
    }

    .modal-content button {
      padding: 0.6rem 1.2rem;
      font-weight: bold;
      border: none;
      border-radius: 8px;
      cursor: pointer;
    }

    .btn-submit {
      background-color: #00bcd4;
      color: #fff;
    }

    .btn-cancel {
      background-color: #444;
      color: #fff;
      margin-left: 0.5rem;
    }

    @media (max-width: 500px) {
      header h1 {
        font-size: 1.2rem;
      }
    }
  </style>
</head>
<body>

  <header>
    <h1>My Code Projects</h1>
    <button class="btn-new" onclick="openModal()">+ New Project</button>
  </header>

  <div class="container">
    <div class="projects-grid" id="projectsGrid"></div>
  </div>

  <footer>
    &copy; 2025 Your Name | Built with 💻 + 🚀
  </footer>

  <!-- Modal -->
  <div class="modal" id="projectModal">
    <div class="modal-content">
      <h3>Add New Project</h3>
      <input type="text" id="projectTitle" placeholder="Project Title" />
      <textarea id="projectDesc" placeholder="Project Description" rows="3"></textarea>
      <input type="text" id="projectTags" placeholder="Tags (comma-separated)" />
      <input type="url" id="projectLink" placeholder="GitHub Link (optional)" />
      <input type="file" id="projectImage" accept="image/*" />
      <button class="btn-submit" onclick="addProject()">Add</button>
      <button class="btn-cancel" onclick="closeModal()">Cancel</button>
    </div>
  </div>

  <script>
    const modal = document.getElementById('projectModal');
    const grid = document.getElementById('projectsGrid');

    function openModal() {
      modal.style.display = 'flex';
    }

    function closeModal() {
      modal.style.display = 'none';
      document.getElementById('projectTitle').value = '';
      document.getElementById('projectDesc').value = '';
      document.getElementById('projectTags').value = '';
      document.getElementById('projectLink').value = '';
      document.getElementById('projectImage').value = '';
    }

    function saveProjects(projects) {
      localStorage.setItem('myProjects', JSON.stringify(projects));
    }

    function loadProjects() {
      const data = localStorage.getItem('myProjects');
      return data ? JSON.parse(data) : [];
    }

    function renderProjects() {
      grid.innerHTML = '';
      const projects = loadProjects();
      projects.forEach(proj => {
        const card = document.createElement('div');
        card.className = 'project-card';

        let tagsHtml = '';
        if (proj.tags && proj.tags.length > 0) {
          tagsHtml = '<div class="tags">' +
            proj.tags.map(tag => `<span class="tag">${tag}</span>`).join('') +
            '</div>';
        }

        card.innerHTML = `
          ${proj.image ? `<img src="${proj.image}" alt="project image" />` : ''}
          <h2>${proj.title}</h2>
          <p>${proj.description}</p>
          ${proj.link ? `<a href="${proj.link}" target="_blank">🔗 View on GitHub</a>` : ''}
          ${tagsHtml}
        `;
        grid.appendChild(card);
      });
    }

    function addProject() {
      const title = document.getElementById('projectTitle').value.trim();
      const desc = document.getElementById('projectDesc').value.trim();
      const tags = document.getElementById('projectTags').value.trim().split(',').map(t => t.trim()).filter(Boolean);
      const link = document.getElementById('projectLink').value.trim();
      const imageFile = document.getElementById('projectImage').files[0];

      if (!title || !desc) {
        alert("Please enter both title and description.");
        return;
      }

      if (imageFile) {
        const reader = new FileReader();
        reader.onload = function(e) {
          const imageData = e.target.result;
          saveNewProject({ title, description: desc, tags, link, image: imageData });
        };
        reader.readAsDataURL(imageFile);
      } else {
        saveNewProject({ title, description: desc, tags, link, image: null });
      }
    }

    function saveNewProject(project) {
      const projects = loadProjects();
      projects.unshift(project); // newest on top
      saveProjects(projects);
      renderProjects();
      closeModal();
    }

    window.onload = renderProjects;

    window.onclick = function(event) {
      if (event.target === modal) {
        closeModal();
      }
    };
  </script>

</body>
</html>
