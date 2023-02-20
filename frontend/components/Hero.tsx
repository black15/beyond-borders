const Hero = () => {
  return (
	<section className={`relative bg-[url(../public/img/hero.jpg)] bg-cover bg-center bg-no-repeat`}>
	<div className="absolute inset-0 bg-white/75 sm:bg-transparent sm:bg-gradient-to-r sm:from-white/5 sm:to-white/10">
		
	</div>

  	<div className="relative mx-auto max-w-screen-xl px-4 py-32 sm:px-6 lg:flex lg:items-center lg:px-8">
    	<div className="max-w-xl text-center sm:text-left my-12">
      	<h1 className="text-3xl font-extrabold sm:text-5xl py-2 text-gray-300">
        	Get your item
				<span className="block font-extrabold text-rose-700 py-1">
					From Home.
				</span>
			</h1>

			<p className="mt-4 max-w-lg sm:text-xl sm:leading-relaxed text-gray-300">
			Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nesciunt illo
			tenetur fuga ducimus numquam ea!
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