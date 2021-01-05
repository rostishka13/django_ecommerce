 


 <script type="text/javascript">
        let thumb = document.getElementsByClassName('thumb')

        let activeImages = document.getElementsByClassName('active')

        for (var i=0; i < thumb.length; i++){

            thumb[i].addEventListener('mouseover', function(){
                console.log(activeImages)
                
                if (activeImages.length > 0){
                    activeImages[0].classList.remove('active')
                }
                

                this.classList.add('active')
                document.getElementById('featured').src = this.src
            })
        }


        let buttonRight = document.getElementById('slideRight');
        let buttonLeft = document.getElementById('slideLeft');

        buttonLeft.addEventListener('click', function(){
            document.getElementById('slider').scrollLeft -= 180
        })

        buttonRight.addEventListener('click', function(){
            document.getElementById('slider').scrollLeft += 180
        })


    </script> 