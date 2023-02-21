const Hero = () => {
  return (
	<section className={`relative bg-[url(../public/img/hero.jpg)] bg-cover bg-center bg-no-repeat`}>
		<div className="absolute inset-0 sm:bg-transparent sm:bg-gradient-to-r from-white/5 to-white/10"></div>
		<div className="relative mx-auto max-w-screen-xl px-4 py-32 sm:px-6 lg:flex lg:items-center lg:px-8">
			<div className="max-w-xl text-center sm:text-left my-24">
				<h1 className="text-3xl font-extrabold sm:text-5xl py-2 text-gray-300">
				Get your item
					<span className="block font-extrabold text-rose-700 py-1">
						From Home.
					</span>
				</h1>
				<p className="mt-4 max-w-md sm:text-xl sm:leading-relaxed text-gray-300">
					You can get your item now, from all arround the world by contacting algerian residents
				</p>
				<div className="mt-8 flex flex-wrap gap-4 text-center">
					<a
						href="#"
						className="block w-full rounded bg-rose-600 px-12 py-3 text-sm font-medium text-white shadow hover:bg-rose-700 focus:outline-none focus:ring active:bg-rose-500 sm:w-auto">
						Get Started
					</a>
					<a
						href="#"
						className="block w-full rounded bg-white px-12 py-3 text-sm font-medium text-rose-600 shadow hover:text-rose-700 focus:outline-none focus:ring active:text-rose-500 sm:w-auto">
						Learn More
					</a>
				</div>
			</div>
		</div>
	</section>
  )
}

export default Hero