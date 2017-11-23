from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ModelForm

from check.core.models import Cliente, Fornecedor, Banco, Terceiro


class CustomFormHelper(FormHelper):
    form_method = 'post'
    form_class = 'form-group'

    def __init__(self, *args, **kwargs):
        super(CustomFormHelper, self).__init__(*args, **kwargs)
        self.add_input(Submit('submit', 'Salvar'))


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        self.helper = CustomFormHelper()



class FornecedorForm(ModelForm):
    class Meta:
        model = Fornecedor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(FornecedorForm, self).__init__(*args, **kwargs)
        self.helper = CustomFormHelper()
        
        
class BancoForm(ModelForm):
    class Meta:
        model = Banco
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(BancoForm, self).__init__(*args, **kwargs)
        self.helper = CustomFormHelper()
        
class TerceiroForm(ModelForm):
    class Meta:
        model = Terceiro
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TerceiroForm, self).__init__(*args, **kwargs)
        self.helper = CustomFormHelper()