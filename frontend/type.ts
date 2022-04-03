import { IconType } from "react-icons";

export interface Service {
  title: string;
  about: string;
  Icon: IconType;
}

export interface Skill {
  name: string;
  level: string;
  Icon: IconType;
}

export interface Project {
  id: number;
  name: string;
  description: string;
  get_image: string;
  get_thumbnail: string;
  deployed_url: string;
  github_url: string;
  categories: string[];
  key_techs: string[];
}
