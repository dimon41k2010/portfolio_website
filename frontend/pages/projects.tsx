import { useState } from "react";
import ProjectCard from "../components/ProjectCard";
import ProjectNavbar from "../components/ProjectsNavbar";
// import { projects as projectsData } from "../data";
import { motion } from "framer-motion";
import { stagger, fadeInUp, routeAnimation } from "../animation";
import { GetServerSidePropsContext } from "next";

const Projects = ({ projectsData, categories }) => {
  const [projects, setProjects] = useState(projectsData);
  const [active, setActive] = useState("all");

  const [showDetail, setShowDetail] = useState<number | null>(null);

  const handleFilterCategory = (category: string | "all") => {
    if (category === "all") {
      setProjects(projectsData);
      setActive(category);
      return;
    }
    const newArray = projectsData.filter((project) =>
      project.categories.includes(category)
    );
    setProjects(newArray);
    setActive(category);
  };
  return (
    <motion.div
      className="px-5 py-2 overflow-y-scroll1"
      style={{ height: "600px" }}
      variants={routeAnimation}
      initial="initial"
      animate="animate"
      exit="exit"
    >
      <ProjectNavbar
        handleFilterCategory={handleFilterCategory}
        active={active}
        categories={categories}
      />

      <motion.div
        className="relative grid grid-cols-12 gap-4 my-3"
        variants={stagger}
        initial="initial"
        animate="animate"
      >
        {projects.map((project) => (
          <motion.div
            className="col-span-12 p-2 bg-gray-200 rounded-lg sm:col-span-6 lg:col-span-4 dark:bg-dark-200"
            variants={fadeInUp}
          >
            <ProjectCard
              project={project}
              key={project.name}
              showDetail={showDetail}
              setShowDetail={setShowDetail}
            />
          </motion.div>
        ))}
      </motion.div>
    </motion.div>
  );
};

export default Projects;

export const getServerSideProps = async (
  context: GetServerSidePropsContext
) => {
  const resProject = await fetch("http://localhost:8000/api/v1/project");
  const dataProject = await resProject.json();

  const resCategories = await fetch(
    "http://localhost:8000/api/v1/project/category"
  );
  const dataCategories = await resCategories.json();
  console.log(dataCategories);
  return {
    props: {
      projectsData: dataProject,
      categories: dataCategories,
    },
  };
};
