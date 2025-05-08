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
    <form onSubmit={handleSubmit} className="conversion-bar">
      <input
        type="url"
        name="url"
        placeholder="Entrez l'URL"
        value={form.url}
        onChange={handleChange}
        required
        className="flex-1 px-4 py-2 rounded border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"
      />

      <input
        type="text"
        name="lang"
        placeholder="Langue (fr, en, etc.)"
        value={form.lang}
        onChange={handleChange}
        className="w-32 px-4 py-2 rounded border border-gray-300"
      />

      <input
        type="text"
        name="name"
        placeholder="Nom personnalisé"
        value={form.name}
        onChange={handleChange}
        className="w-40 px-4 py-2 rounded border border-gray-300"
      />

      <select
        name="format"
        value={form.format}
        onChange={handleChange}
        className="w-28 px-3 py-2 rounded border border-gray-300">
        <option value="txt">.txt</option>
        <option value="json">.json</option>
      </select>

      <button type="submit" className="convert-button">Scrape</button>
    </form>
  );
};

export default ScraperBar;
