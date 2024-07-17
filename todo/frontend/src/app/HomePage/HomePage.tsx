import { useEffect } from "react";
import { useRouter } from "next/router";
import axios from "axios";

const HomePage: React.FC = () => {
  const router = useRouter();

  useEffect(() => {
    const checkAuth = async () => {
      try {
        const response = await axios.get("/api/check-auth");
        if (response.status !== 200) {
          router.push("/login");
        }
      } catch (error) {
        router.push("/login");
      }
    };
    checkAuth();
  }, [router]);

  return <div>Home Page Content</div>;
};

export default HomePage;
