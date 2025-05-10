import React, { useState } from "react";
import { FaSyncAlt } from "react-icons/fa";

import "../styles/ScraperBar.css";

const ScraperBar = () => {

  const [form, setForm] = useState({
    url: "",
    lang: "",
    name: "",
    format: "txt",
  });
  

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };


  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log("Données envoyées :", form);
    // TODO : Appel API ici (POST /scrape)
  };

  return (
    <form onSubmit={handleSubmit} className="scraper-bar">
      <input
        type="url"
        name="url"
        placeholder="Entrez l'URL"
        value={form.url}
        onChange={handleChange}
        required
        className="url-input"
      />

      <input
        type="text"
        name="lang"
        placeholder="Langue (fr, en, etc.)"
        value={form.lang}
        onChange={handleChange}
        className="lang-input"
      />

      <input
        type="text"
        name="name"
        placeholder="Nom personnalisé"
        value={form.name}
        onChange={handleChange}
        className="name-input"
      />

      <select
        name="format"
        value={form.format}
        onChange={handleChange}
        className="format-select">
        <option value="txt">.txt</option>
        <option value="json">.json</option>
      </select>

      <button type="submit" className="convert-button">Scrape</button>
    </form>
  );
};

export default ScraperBar;
