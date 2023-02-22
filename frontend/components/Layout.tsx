import Footer from "./snippets/Footer";
import Header from "./snippets/Header";

type LayoutProps = {
	children: React.ReactNode,
 };
 
 export default function Layout({ children }: LayoutProps) {
	return (
	  	<main className="">
			<Header />
			{children}
			<Footer />
	  	</main>

	);
 }