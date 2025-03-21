import { useState } from "react";
import { Button } from "./components/ui/Button";
import { Input } from "./components/ui/input";
import { Textarea } from "./components/ui/textArea";
import { Card, CardContent } from "./components/ui/card";
import { Upload } from "lucide-react";
import axios from "axios";

export default function ResumeScreeningApp() {
  const [resume, setResume] = useState(null);
  const [title, setTitle] = useState("");
  const [minExperience, setMinExperience] = useState("");
  const [requiredSkills, setRequiredSkills] = useState("");
  const [level, setLevel] = useState("");
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setResume(e.target.files[0]);
  };

  const handleSubmit = async () => {
    if (!resume || !title || !minExperience || !requiredSkills || !level) {
      alert("Please fill in all fields and upload a resume.");
      return;
    }

    const formData = new FormData();
    formData.append("resume", resume);
    formData.append("title", title);
    formData.append("min_experience", minExperience);
    formData.append("required_skills", requiredSkills);
    formData.append("level", level);

    setLoading(true);
    try {
      const res = await axios.post("http://localhost:8000/screen-resume/", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setResponse(res.data);
    } catch (error) {
      console.error("Error screening resume:", error);
      alert("Failed to process resume.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex h-screen">
      {/* Sidebar */}
      <div className="w-2/4 bg-gray-100 p-6 flex flex-col gap-4">
        <h2 className="text-xl font-bold">Upload your resume in pdf format</h2>
        <Input type="file" accept=".pdf" onChange={handleFileChange} />
        <h2 className="text-xl font-bold">Job Description</h2>
        <Input placeholder="Job Title (e.g. Software Engineer)" value={title} onChange={(e) => setTitle(e.target.value)} />
        <Input type="number" placeholder="Min Experience (in years)" value={minExperience} onChange={(e) => setMinExperience(e.target.value)} />
        <Textarea placeholder="Required Skills (e.g. Python, SQL, etc.)" value={requiredSkills} onChange={(e) => setRequiredSkills(e.target.value)} />
        <Input placeholder="Job Level (e.g. Junior, Mid, Senior)" value={level} onChange={(e) => setLevel(e.target.value)} />
        <Button onClick={handleSubmit} disabled={loading} className="mt-4">
          {loading ? "Processing..." : "Submit"}
        </Button>
      </div>

      {/* Chat Response */}
      <div className="flex-1 flex items-center justify-center p-6">
        {response ? (
          <Card className="w-full">
            <CardContent className="p-6">
              <h2 className="text-xl font-bold mb-4">Screening Result</h2>
              {/* <p><strong>Status:</strong> {response.status}</p> */}
              <p> {response.result}</p>
              {response.error && <p className="text-red-500"><strong>Error:</strong> {response.error}</p>}
            </CardContent>
          </Card>
        ) : (
          <p className="text-gray-500">Submit a resume to get started.</p>
        )}
      </div>
    </div>
  );
}